from .graphdb import gdb
from logzero import logger


campaigns_test = [
  {
    "campaign": "Campaign1",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign Totals": {
      "Actual Goal": "785",
      "Conversion Rate": 55.55,
      "Starting Budget": 500.50,
      "Cost": 275.45,
      "Improvements Cost": 150,
      "Success Fee": 75.50,
      "Budget Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign2",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign Totals": {
      "Actual Goal": "785",
      "Conversion Rate": 55.55,
      "Starting Budget": 500.50,
      "Cost": 275.45,
      "Improvements Cost": 150,
      "Success Fee": 75.50,
      "Budget Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign3",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign Totals": {
      "Actual Goal": "785",
      "Conversion Rate": 55.55,
      "Starting Budget": 500.50,
      "Cost": 275.45,
      "Improvements Cost": 150,
      "Success Fee": 75.50,
      "Budget Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign4",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign Totals": {
      "Actual Goal": "785",
      "Conversion Rate": 55.55,
      "Starting Budget": 500.50,
      "Cost": 275.45,
      "Improvements Cost": 150,
      "Success Fee": 75.50,
      "Budget Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign5",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign Totals": {
      "Actual Goal": "785",
      "Conversion Rate": 55.55,
      "Starting Budget": 500.50,
      "Cost": 275.45,
      "Improvements Cost": 150,
      "Success Fee": 75.50,
      "Budget Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign6",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign Totals": {
      "Actual Goal": "785",
      "Conversion Rate": 55.55,
      "Starting Budget": 500.50,
      "Cost": 275.45,
      "Improvements Cost": 150,
      "Success Fee": 75.50,
      "Budget Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign7",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign Totals": {
      "Actual Goal": "785",
      "Conversion Rate": 55.55,
      "Starting Budget": 500.50,
      "Cost": 275.45,
      "Improvements Cost": 150,
      "Success Fee": 75.50,
      "Budget Rollover": 2.50
    }
  },
  {
    "campaign": "Campaign8",
    "industry": "xxx",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted Goal": {
      "Top": 999,
      "Ideal": 777,
      "Low": 555
    },
    "Campaign Totals": {
      "Actual Goal": "785",
      "Conversion Rate": 55.55,
      "Starting Budget": 500.50,
      "Cost": 275.45,
      "Improvements Cost": 150,
      "Success Fee": 75.50,
      "Budget Rollover": 2.50
    }
  }
]


def get_campaigns_test():
    return campaigns_test


def get_campaigns():
    logger.info("CALL /tet/v1/campaigns - BANANAS")
    graph = gdb.get_db()
    data = graph.data("MATCH(c: CAMPAIGN) RETURN c.industry as industry , c.ref as ref , c.target as target, \
    c.touchpoints as touchpoints, c.ActualGoal  as ActualGoal, c.BudgetRollover as BudgetRollover, \
    c.ConversionRate  as ConversionRate, c.Cost  as Cost, c.ImprovementsCost as ImprovementsCost, \
    c.Predicted_Goal  as Predicted_Goal, c.Predicted_Goal_variance as Predicted_Goal_variance, \
    c.StartingBudget as StartingBudget, c.SuccessFee as SuccessFee, c.campaign  as campaign")

    # for elem in data:
    #     print("Element : {}".format(elem))
    return data
