from epi_spam import EpiSpam

if __name__ == '__main__':
    spam_requester = EpiSpam()
    # These three variables compose the link:
    clientId = 'insert_clientid'
    recipientId = 'insert_email'
    recipientListId = 'insert_recipientListId'
    spam = 1
    spam_grund = 'test test test'

    response= spam_requester.post_spam_reason(
        clientId, recipientListId, recipientId, spam, spam_grund)
        
    print(response)
