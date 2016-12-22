import sys
from wit import Wit
import uuid
import traceback


# if len(sys.argv) != 2:
#     print('usage:printhen_wit' + ' <message>')
#     exit(1)
access_token = "4ZRPENNQTQDZ42TCLQOR5ZBIWBTZEJFO"

# Quickstart example
# See https://wit.ai/ar7hur/Quickstart

def first_entity_value(entities, entity,index):
    try:
        if entity not in entities:
            return None
        val = entities[entity][index]['value']
        if not val:
            return None
        return val['value'] if isinstance(val, dict) else val
    except Exception,err:
        return traceback.print_exc()

def send(request, response):
    try:
        print(response['text'])
    except Exception,err:
        print traceback.print_exc()

def extract_value(request):
    try:
        print "extract value executing"
        context = request['context']
        entities  = request['entities']
        copies = first_entity_value(entities,'copies',0)
        page = first_entity_value(entities,'page',0)
        onesided = first_entity_value(entities,'oneside',0)
        if copies:
            context['copies'] = str(copies)
        else:
            context['copies'] = '1'
        
        if page:
            context['page'] = str(page)
            
        else:
            context['page'] = str(first_entity_value(entities,'number',0))
        if onesided:
            context['onesided'] = True
        else:
            context['onesided'] = False
        
        if (context['page']=='None'):
            context['page'] = '-1'
        return context
    except Exception,err:
        return traceback.print_exc()

def extract_value_whole_doc(request):
    try:
        print "extract Whole doc executing"
        context = request['context']
        entities  = request['entities']
        copies = first_entity_value(entities,'copies',0)
        onesided = first_entity_value(entities,'oneside',0)
        if copies:
            context['copies'] = str(copies)
        else:
            context['copies'] = '1'
        
        context['page'] = '-1'
        if onesided:
            context['onesided'] = True
        else:
            context['onesided'] = False
        return context
    except Exception,err:
        return traceback.print_exc()
    
def extract_value_to_from(request):
    try:
        print "extract from to  executing"
        context = request['context']
        entities = request['entities']
        #print "context"
        #print context
        #print "entities"
        #print entities
        copies = first_entity_value(entities,'copies',0)
        from_page = first_entity_value(entities,'from',0)
        to_page = first_entity_value(entities,'to',0)
        onesided = first_entity_value(entities,'oneside',0)
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
        
        if onesided:
            context['onesided'] = True
        else:
            context['onesided'] = False
        return context
    except Exception,err:
        return traceback.print_exc()



actions = {
    'send': send,
    'extract_value_to_from': extract_value_to_from,
    'extract_value':extract_value,
    'extract_value_whole_doc':extract_value_whole_doc,
}

def extract_information(sentence):
    try:
        context={}
        client = Wit(access_token=access_token, actions=actions)
        session = uuid.uuid4()
        #client.interactive()
        #resp = client.message(sys.argv[1])
        context = client.run_actions(session,sentence, context,5)
        print(str(context))
        return context
    except Exception,err:
        return traceback.print_exc()




if __name__ == "__main__":
    sentence = raw_input("Enter your Command")
    extract_information(sentence)
