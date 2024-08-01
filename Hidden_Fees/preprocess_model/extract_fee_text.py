import spacy

def extract_info(text, tables):
    print('nice')
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    
    #MAY HAVE TO TRAIN OUR OWN MODEL OR FIND ANOTHER WAY OF PARSING THROUGH THE VALUES
    #MAYBE USE SOME SORT OF AI TO FIND THE VALUES WITHIN THE PDF FOR YOU 
    # for ent in doc.ents:
    #     if ent.label_ == 'PERCENT':
    #         print(f'Percentage: {ent.text}')
    #     elif ent.label_ == 'MONEY':
    #         print(f'Money: {ent.text}')
    # print(text)
    # print(tables)