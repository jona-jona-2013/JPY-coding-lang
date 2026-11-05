class codeReader():
    varsINT = []
    varsSTR = []
    varsBOOL = []

    def __init__(self, code):
        if code != "":
            self.tokenValue = self.tokenEvaluator(code)

            if self.tokenValue != "":
                if self.tokenValue == "int":
                    print(code)

                elif self.tokenValue == "bool":
                    print(code)

                elif self.tokenValue == "str":
                    if code.startswith("int "):
                        try:
                            EqualsPOS = code.find("=")
                            beforeEqual = EqualsPOS - 1
                            AfterEqual = EqualsPOS + 1

                            self.varsINT.append(code[4:beforeEqual].strip())
                            self.varsINT.append(int(code[AfterEqual:]))

                        except:
                            print("ValueError, did you forget to give it a value? Or perphaps you made the value not an int?")

                    elif code.startswith("str "):
                        try:
                            EqualsPOS = code.find("=")
                            beforeEqual = EqualsPOS - 1
                            AfterEqual = EqualsPOS + 1

                            self.varsSTR.append(code[4:beforeEqual])
                            self.varsSTR.append(str(code[AfterEqual:]))

                        except:
                            print("ValueError, did you forget to give it a value?")

                    elif code.startswith("bool "):
                        try:
                            EqualsPOS = code.find("=")
                            beforeEqual = EqualsPOS - 1
                            AfterEqual = EqualsPOS + 1

                            self.varsBOOL.append(code[5:beforeEqual])
                            self.varsBOOL.append(bool(code[AfterEqual:]))

                        except ValueError:
                            pass

                    elif code == ("printINT()"):
                        print(self.varsINT)

                    elif code == ("printSTR()"):
                        print(self.varsSTR)

                    elif code == ("printBOOL()"):
                        print(self.varsBOOL)

                    elif code == ("printVARS()"):
                        print(self.varsINT)
                        print(self.varsSTR)
                        print(self.varsBOOL)

                    else:
                        try:
                            self.varLocation = self.varsINT.index(code)
                            print(self.varsINT[self.varLocation + 1])
                    
                        except ValueError:
                            try:
                                self.varLocation = self.varsSTR.index(code)
                                print(self.varsSTR[self.varLocation + 1])

                            except ValueError:
                                try:
                                    self.varLocation = self.varsBOOL.index(code)
                                    print(self.varsBOOL[self.varLocation + 1])

                                except ValueError:
                                    pass

    def tokenEvaluator(self, code):
        tokenValue = ""
        try:
            int(code)
            tokenValue = "int"

        except ValueError:
            if code == "true" or code == "false":
                tokenValue = "bool"

            else:
                tokenValue = "str"

        return tokenValue