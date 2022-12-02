import praw
from cognitive_function import *

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="<Console:Frosty:1.0>",
    username="",
)


def parse_input(comment):
    print(comment.body)
    cog_inp = comment.body.lower()
    cog_inp = cog_inp.replace('u/imaginary_outcome47', '')
    cog_inp = cog_inp.split(',')
    return cog_inp

def error_check(comment, cog_inp):
    errors = 0

    if len(cog_inp) != 8:
        reply_error(comment)
        errors = 1

    for i in cog_inp:
        if i.isnumeric == False:
            reply_error(comment)
            errors = 1

    return errors

def reply_error(comment):
    comment.reply(body="Enter your Cognitive function in order the order \n\n Ne, Ni, Se, Si, Te, Ti, Fe, Fi")
    comment.mark_read()
    print('error')

def main():
    comments = reddit.inbox.stream()
    print('getting comments')

    for comment in comments:
        try:
            if (comment in reddit.inbox.mentions() or comment in reddit.inbox.comment_replies()) and comment in reddit.inbox.unread():
                cog_inp = parse_input(comment)
                
                if error_check(comment, cog_inp) == 0:
                    print(cog_inp)

                    reply_com = cog_main(cog_inp)
                    comment.reply(body=reply_com)
                    comment.mark_read()

                    print('noice')

        except praw.exceptions.APIException as error:
            print(error)

if __name__ == '__main__':
    main()
