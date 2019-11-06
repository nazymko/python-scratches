import random
import string
import csv

images = [
    "https://static.tildacdn.com/tild3661-3236-4665-b337-393664303233/14x.png",
    "https://static.tildacdn.com/tild6533-3062-4137-a162-626132333364/24x.png",
    "https://static.tildacdn.com/tild6235-3333-4436-b834-633935656133/34x.png",
    "https://static.tildacdn.com/tild3037-3235-4833-a634-663161616563/64x.png",
    "https://static.tildacdn.com/tild6337-3764-4630-b363-356661316235/84x.png",
    "https://static.tildacdn.com/tild3861-3336-4439-b666-666435633431/74x.png",
    "https://static.tildacdn.com/tild6239-3033-4131-b038-386430373932/94x.png",
    "https://static.tildacdn.com/tild3266-6234-4033-a438-313165376633/104x.png",
]


# require 2 items in text
def random_text(folder, max_skills=4):
    file = open(folder + "/skills", "r")
    read_lines = file.readlines()
    clean_lines = []
    for it in read_lines:
        clean_lines.insert(1, it.replace("\n", ""))

    choices = random.choices(clean_lines, k=max_skills)

    content_text_file = open(folder + "/text", "r")
    content = content_text_file.read()
    part_1 = ""
    for it in range(max_skills):
        if it < max_skills - 2:
            part_1 = part_1 + choices[it] + ", "
        elif it < max_skills - 1:
            part_1 = part_1 + choices[it]

    part_2 = "" + choices[max_skills - 1]
    content = content.replace("{1}", part_1)
    content = content.replace("{2}", part_2)
    return {
        "content": content,
        "choices": choices
    }


def mix_text(folder, max_items=6, max_skills=4):
    all_texts = []
    for i in range(max_items):
        all_texts.insert(1, random_text(folder, max_skills))
    return all_texts


file_name = "content.csv"
file = open(file_name, "w+")
file.close()


def print_csv_line(file_name, department, title, content, tech_stack):
    opened_file = open(file_name, "a+")
    writer = csv.writer(opened_file)
    # opened_file.write(line)

    writer.writerow(
        ["", "", department, title, "Experienced {}".format(title), content, random.choice(images), "", "", "", "",
         ", ".join(tech_stack)])  # append/write row to file

    opened_file.flush()
    opened_file.close()
    pass


def print_depatment_part(clection, department="Development", title="angular developers"):
    for element in clection:
        print_csv_line(file_name, department, title, element["content"], element["choices"])
    pass


# mix_text("backend", 4, 5)
# mix_text("front_end", 6, 6)
# mix_text("front_end_2", 6, 6)
# mix_text("front_end_3", 6, 6)
# mix_text("front_end_4", 6, 6)
# mix_text("mobile", 4, 5)
# mix_text("games", 4, 5)

print_depatment_part(mix_text("backend", 4, 6), department="Development", title="software developers")
print_depatment_part(mix_text("front_end_4", 4, 6), department="Front End", title="Vue.js developers")
print_depatment_part(mix_text("front_end_3", 4, 6), department="Front End", title="Node.js developers")
print_depatment_part(mix_text("front_end_2", 4, 6), department="Front End", title="Ember.js developers")
print_depatment_part(mix_text("front_end", 4, 6), department="Front End", title="Angular.js developers")
print_depatment_part(mix_text("mobile", 4, 6), department="Mobile Department",
                     title="mobile developers (Androind & iOS)")
