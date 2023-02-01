



def getNiceName(author):
    if author.nick:
        return str(author.nick)
    else:
        return str(author.name)


def extractMemberIdList(_message):
    import re, pprint

    print("extractMemberIdList(\"" + _message + "\");")

    # input_example = "creerChannel <False news=False category_id=859361778303369246> type=<MessageType.default: 0> author=<Member id=326707820835897354 name='cosmogonies' discriminator='6114' bot=False nick='Kraken Sj��var (4)' guild=<Guild id=849369853491806288 name='InaugurationMus��eFlottant' shard_id=None chunked=False member_count=15>> flags=<MessageFlags value=0>>creerChannel <Message id=666 channel=<TextChannel id=860169722556579860 name='capitaine-conteur' position=3 nsfw=False news=False category_id=859361778303369246> type=<MessageType.default: 0> author=<Member id=666 name='cosmogonies' discriminator='6114' bot=False nick='Kraken Sj��var (4)' guild=<Guild id=849369853491806288 name='InaugurationMus��eFlottant' shard_id=None chunked=False member_count=15>> flags=<MessageFlags value=0>>   <Member id=123 n  "
    # pattern = re.compile(r'Member id=([0-9]+)')
    pattern = re.compile(r'@!([0-9]+)')
    resultMatch = pattern.findall(_message)
    print("resultMatch=");
    pprint.pprint(resultMatch)

    memberIdList = []
    for group in resultMatch:
        pprint.pprint(group)
        memberIdList.append(int(group))
    return memberIdList