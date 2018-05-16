import random


class schedule:
    count_days = 5

    count_classes = 3

    count_lessons_day = 5

    lessons = ["Ukraine language", "Math", "Natural science", "Health", "Physical raining"]

    days = [[] for i in range(count_days)]

    def __init__(self, pr=True):

        if (pr):
            for i in range(self.count_days):
                for j in range(self.count_classes):
                    day_schedule_class = []
                    for t in range(self.count_lessons_day):
                        k = random.randint(0, len(self.lessons) - 1)
                        day_schedule_class.append(self.lessons[k])
                    self.days[i].append(day_schedule_class)
                    # random create shedule
                #


        else:
            pass

    def __str__(self):

        header_line = "Monday | Tuestday| Wednesday | Thursday | Friday\n";

        return self.days.__str__()

    def get_health(self):
        pass

    def mutate(self):
        pass


a = schedule()

print(a)