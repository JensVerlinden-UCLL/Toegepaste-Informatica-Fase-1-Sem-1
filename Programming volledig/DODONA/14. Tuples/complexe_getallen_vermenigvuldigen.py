# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/1180618752

def product(tuple1, tuple2):

    real = tuple1[0] * tuple2[0] - tuple1[1] * tuple2[1]
    imag = tuple1[0] * tuple2[1] + tuple1[1] * tuple2[0]

    return (real, imag)

