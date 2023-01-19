# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/1567511933

def afvlakken(setje):

    setlijst = []

    for i in setje:

        if isinstance(i, int):
            setlijst.append(i)

        else:
            sublijst = afvlakken(i)
            setlijst.extend(sublijst)

    return tuple(setlijst)
