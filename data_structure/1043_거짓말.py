# https://www.acmicpc.net/problem/1043
import sys

cnt_party = int(sys.stdin.readline().split()[1])
know_people = set(sys.stdin.readline().split()[1:])
party_list = [None for _ in range(cnt_party)]
is_possible = [1 for _ in range(cnt_party)]

for i in range(cnt_party):
    party_list[i] = set(sys.stdin.readline().split()[1:])
    
for _ in range(cnt_party):
    for i, party in enumerate(party_list):
        if is_possible[i] == 1:
            union = know_people.union(party)
            have_intersection = len(union) < len(know_people) + len(party)
            if have_intersection:
                is_possible[i] = 0
                know_people = union

print(sum(is_possible))