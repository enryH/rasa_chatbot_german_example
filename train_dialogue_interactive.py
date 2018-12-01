from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy

from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.training import interactive
from rasa_core.utils import EndpointConfig

import keras


# FALLBACK_THRESHOLD = 0.5  

def run_bot_online(interpreter,
                   domain_file="domain.yml",
                   training_data_file='data/stories.md',
                   model_path = './models/dialogue'):
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

    fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                              core_threshold = 0.5,
                              nlu_threshold  = 0.5)

    agent = Agent(domain      = domain_file,
                  policies    = [MemoizationPolicy(), KerasPolicy(), fallback],
                  interpreter = interpreter,
				  action_endpoint = action_endpoint
                  )
    
    earlystopping = keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0,
                                                  patience=2, 
                                                  verbose=0,
                                                  mode='auto', 
                                                # only in newer keras version available:  
                                                #   baseline=None, 
                                                #   restore_best_weights=True
                                                #
                                                 )				  
    
    
    data = agent.load_data(training_data_file)
    agent.train(data,
                # batch_size=25,
                # epochs=300,
                # max_training_samples=1000,
                validation_split = 0.1,
                callbacks = [earlystopping]
                )

    agent.persist(model_path)
    interactive.run_interactive_learning( agent, stories = "data/stories.md",
                                            finetune=False,
                                            serve_forever=True,
                                            skip_visualization=True)
    return agent


if __name__ == '__main__':
    # logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/versicherung_nlu')
    run_bot_online(nlu_interpreter)


