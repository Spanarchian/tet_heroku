from .graphdb import gdb
from logzero import logger

test_audience = [
]


def get_test_audience():
    return test_audience


def get_audience():
    logger.info("CALL /tet/v1/audience")
    graph = gdb.get_db()
    data = graph.data(
      "MATCH(a: AUDIENCE) RETURN a.twitter as twitter, a.ref as ref, a.gender as gender, a.phone as phone, \
      a.age_group as age_group, a.income_lvl as income_lvl, a.postcode_lvl as postcode_lvl, a.psyc_lvl as psyc_lvl, \
      a.edu_lvl as edu_lvl, a.email as email, a.behav_lvl as behav_lvl"
    )

    # for elem in data:
    #     print("Element : {}".format(elem))
    return data



