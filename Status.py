import Patient
# status 1 = the patient tested positive to covid 19 , confirmed patient
# status 0 = the patient was positive before but tested negative now and the patient recovered
# if the patient was never positive and tested negative now,the patient will not be added to the system


def status_change(self):
    num = 0
    print("if the result is positive enter 1, if negative enter 0")
    result = input(num)
    if result == 1:
        status = 1  # status 1 = confirmed patient
        return status
    elif result == 0:
        if self.test != 1:
            status = 0
            return status

    else:
        print("error, wrong input")


