import sys
from wit import Wit
import uuid

# if len(sys.argv) != 2:
#     print('usage:printhen_wit' + ' <message>')
#     exit(1)
access_token = "4ZRPENNQTQDZ42TCLQOR5ZBIWBTZEJFO"

# Quickstart example
# See https://wit.ai/ar7hur/Quickstart

def first_entity_value(entities, entity,index):
    if entity not in entities:
        return None
    val = entities[entity][index]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    print(response['text'])

def extract_value(request):
    context = request['context']
    entities  = request['entities']
    copies = first_entity_value(entities,'copies',0)
    page = first_entity_value(entities,'page',0)
    if copies:
        context['copies'] = str(copies)
    else:
        context['copies'] = '1'
     
    if page:
        context['page'] = str(page)
        
    else:
        context['page'] = str(first_entity_value(entities,'number',0))
    return context

def extract_value_whole_doc(request):
    context = request['context']
    entities  = request['entities']
    copies = first_entity_value(entities,'copies',0)
    if copies:
        context['copies'] = str(copies)
    else:
        context['copies'] = '1'
     
        context['page'] = '-1'
    return context
    
def extract_value_to_from(request):
    context = request['context']
    entities = request['entities']
    print "context"
    print context
    print "entities"
    print entities
    copies = first_entity_value(entities,'copies',0)
    from_page = first_entity_value(entities,'from',0)
    to_page = first_entity_value(entities,'to',0)
    # loc = first_entity_value(entities, 'location')
    # if loc:
    #     context['forecast'] = 'sunny'
    #     if context.get('missingLocation') is not None:
    #         del context['missingLocation']
    # else:
    #     context['missingLocation'] = True
    #     if context.get('forecast') is not None:
    #         del context['forecast']
    if copies:
        context['copies'] = str(copies)
    else:
        context['copies'] = '1'
     
    if from_page:
        context['from_page'] = str(from_page)
        
    else:
        context['from_page'] = str(first_entity_value(entities,'number',0))
    if to_page:
        context['to_page'] = str(to_page)
    else:
        context['to_page'] = str(first_entity_value(entities,'number',1))
    
    return context


actions = {
    'send': send,
    'extract_value_to_from': extract_value_to_from,
    'extract_value':extract_value,
    'extract_value_whole_doc':extract_value_whole_doc,
}

def extract_information(sentence):
    context={}
    client = Wit(access_token=access_token, actions=actions)
    session = uuid.uuid4()
    #client.interactive()
    #resp = client.message(sys.argv[1])
    context = client.run_actions(session,sentence, context,5)
    print(str(context))
    return context



if __name__ == "__main__":
    sentence = raw_input("Enter your Command")
    extract_information(sentence)
