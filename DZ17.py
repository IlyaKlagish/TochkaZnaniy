
school = {"Аня","Вася","Катя","Дима"}
club = {"Аня","Вася","Петя","Маша"}

common = school & club
print("Общие друзья: ",common)

school_only = school - club
print("Друзья только по школе: ",school_only)

club_only = club - school
print("Друзья только по кружку: ",club_only)

all_friends = school | club
print("Все друзья: ",all_friends)

school.add("Саша")
print("Друзья по школе с Сашей: ",school)

club.discard("Петя")
print("Друзья по кружку без Пети: ",club)