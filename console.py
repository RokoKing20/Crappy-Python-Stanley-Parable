import bored
import view

def main():
    a = view.mode_choose()
    if a == "Yes":
        while bored.points <10 and bored.losing_points < 10 :
            charactetrs = bored.letters
            random_str = bored.random_choose(charactetrs)
            c = view.user_string_task(random_str)
            d = bored.check_user(random_str, c)
            if d == False:
                bored.losing_points = bored.losier_points(bored.losing_points)
                print(bored.points)
                print(bored.losing_points)
            elif d == True:
                bored.points = bored.adding_points(bored.points)
                print(bored.points)
                print(bored.losing_points)
        else:
            if bored.points == 10:
                view.win()
            elif bored.losing_points == 10:
                view.lose()
    elif a == "No":
        view.turend_off()
    else:
        view.rule_breaker()
        main()


main()