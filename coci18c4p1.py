
wand_current_owner = input()
fighting_times = int(input())

wand_records_table = wand_current_owner

for f in range(fighting_times):
    fight_records = input()
    if fight_records[2] == wand_current_owner:
        wand_current_owner = fight_records[0]
        if wand_current_owner not in wand_records_table:
            wand_records_table = wand_records_table + wand_current_owner

# print("wand_current_owner: ", wand_current_owner, ", How_many_the_wand_was_hold: ", len(wand_records_table))
print(wand_current_owner)
print(len(wand_records_table))