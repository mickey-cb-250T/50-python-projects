class predictor:

    team = {}

    print("== welcome to match predictor ==")
    print("1. add your team")
    print("2. add team performance")
    print("3. predict the winner")
    print("4. add player performance")
    print("5. see players performance")
    print("6. exit")


class team_add(predictor):

    def match(self):

        while True:

            self.choose = int(input("Which one you wanna go for: "))

            # ADD TEAM
            if self.choose == 1:

                d = input("Enter your team name: ")

                self.team[d] = {
                    "played": 0,
                    "won": 0,
                    "lost": 0,
                    "players": {}
                }

                print(self.team)

            # TEAM PERFORMANCE
            elif self.choose == 2:

                d = input("Enter team name: ")

                if d in self.team:

                    e = int(input("Enter matches played: "))
                    a = int(input("Enter matches won: "))

                    u = e - a

                    self.team[d]["played"] = e
                    self.team[d]["won"] = a
                    self.team[d]["lost"] = u

                    print(self.team)

                else:
                    print("Team not found!")

            # PREDICTION
            elif self.choose == 3:

                w = input("Enter team 1: ")
                t = input("Enter team 2: ")

                if w in self.team and t in self.team:

                    played_w = self.team[w]["played"]
                    won_w = self.team[w]["won"]

                    played_t = self.team[t]["played"]
                    won_t = self.team[t]["won"]

                    team_w_winrate = (won_w / played_w) * 100
                    team_t_winrate = (won_t / played_t) * 100

                    if team_w_winrate > team_t_winrate:
                        print(f"{w} win rate = {team_w_winrate}%")
                        print(f"Winner = {w}")

                    elif team_t_winrate > team_w_winrate:
                        print(f"{t} win rate = {team_t_winrate}%")
                        print(f"Winner = {t}")

                    else:
                        print("Both teams have the same win rate!")

                else:
                    print("One or both teams not found!")

            # PLAYER PERFORMANCE
            elif self.choose == 4:

                d = input("Enter team name: ")

                if d in self.team:

                    player = input("Enter player name: ")
                    runs = int(input("Enter player's runs: "))
                    strike_rate=float(input("Enter player's strike rate: "))
                    wickets=int(input("Enter players wicket: "))

                    self.team[d]["players"][player] = {
                        "runs": runs,
                        "strike-rate":strike_rate,
                        "wickets":wickets
                    }

                    print(self.team)

                else:
                    print("Team not found!")
            elif self.choose==5:
                print("==welcome to player performance  analysis==")
                
                name=input("enter player name: ")
                if name in self.team[d]["players"]:
                        print(self.team[d]["players"][name])
                        s=(input("wanna see his next match score y/n: "))
                        if s=="y":
                            r=input("enter player name : ")
                            if r in self.team[d]["players"]:
                                q=self.team[d]["players"][r]["runs"]
                                x=self.team[d]["played"]
                                next_match_score=(q/x)
                                print(f"next match score of {r} will be\n{next_match_score}")
                                
                        
            # EXIT
            elif self.choose == 6:
                print("Thank you for using Match Predictor!")
                break


shri = team_add()
shri.match()