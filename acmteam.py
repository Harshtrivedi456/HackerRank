def acmTeam(topic):
    n = len(topic)
    max_topics = 0
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            known = bin(int(topic[i], 2) | int(topic[j], 2)).count('1')
            if known > max_topics:
                max_topics = known
                count = 1
            elif known == max_topics:
                count += 1
    return max_topics, count

if __name__ == "__main__":
    n, m = map(int, input().split())
    topic = [input() for _ in range(n)]
    max_topics, count = acmTeam(topic)
    print(max_topics)
    print(count)
