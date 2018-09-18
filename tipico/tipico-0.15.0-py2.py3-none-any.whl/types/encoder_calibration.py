
class EncoderCalibration(object):

    def __init__(self, coefficients):
        self.coefficients= coefficients


    def encoderToPosition(self, encoderValue):
        return self.coefficients[0] + \
            encoderValue * self.coefficients[1]


