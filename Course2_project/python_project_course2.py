punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(str):
    for i in punctuation_chars:
        str=str.replace(i,"")
    return str

# lists of words to use

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(str):
    count=0
    for i in str.split():
        s=strip_punctuation(i)
        if s.lower() in positive_words:
            count+=1
    return count


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(str):
    count=0
    for i in str.split():
        s=strip_punctuation(i)
        if s.lower() in negative_words:
            count+=1
    return count

data=open("project_twitter_data.csv",'r')
dt=data.readlines()
dt_2=dt[1:]

result=open("resulting_data.csv",'w')

result.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
result.write('\n')

for line in dt_2:
    lst=line.strip().split(",")
    p_score=get_pos(lst[0])
    n_score=get_neg(lst[0])
    net_score=p_score-n_score
    output='{}, {}, {}, {}, {}'.format(lst[1],lst[2],p_score,n_score,net_score)
    result.write(output)  
    result.write('\n')