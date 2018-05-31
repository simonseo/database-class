### Database Design and Web Implementation Assignment #8
# Instructor: Deena Engel
# Student: Simon Seo (ms9144)
# Date: December 8, 2017

##### Problem 1 #####
# How many zip codes are there in your home state?
db.dbw.aggregate(
  [
    { $match: { "state": "NY" } },
    { $group: { "_id": "$state" , "count": { $sum: 1 } } }
  ]
);
# Query Result: { "_id" : "NY", "count" : 1595 }
# Answer: There are 1595 zip codes in NY



##### Problem 2 #####
# List the five least heavily populated zipcodes (those that have the smallest populations) in Georgia. 
# (Hint: Be sure to exclude zip codes with a population of zero; as these data are likely to be missing or incorrect.)
db.dbw.find(
  {"state" : "GA", "pop" : {"$gt" : 0}},
  {"loc" : 0}
).sort(
  {"pop" : 1}
).limit(5)
# Query Result:
# { "_id" : "30346", "city" : "ATLANTA", "pop" : 18, "state" : "GA" }
# { "_id" : "30148", "city" : "MARBLE HILL", "pop" : 98, "state" : "GA" }
# { "_id" : "31743", "city" : "DE SOTO", "pop" : 112, "state" : "GA" }
# { "_id" : "31327", "city" : "SAPELO ISLAND", "pop" : 120, "state" : "GA" }
# { "_id" : "31066", "city" : "MUSELLA", "pop" : 121, "state" : "GA" }
# Answer: The least populated zipcodes in Georgia are 30346, 30148, 31743, 31327, and 31066.



##### Problem 3 #####
# List the zip code and population for three zip codes in the Bronx.
db.dbw.find(
  {"city" : "BRONX"},
  {"_id" : 1, "pop" : 1}
).limit(3)
# Query Result:
# { "_id" : "10451", "pop" : 42854 }
# { "_id" : "10452", "pop" : 55890 }
# { "_id" : "10453", "pop" : 70544 }
# Answer:
# zip    pop
# 10451  42854
# 10452  55890
# 10453  70544



##### Problem 4 #####
# How many zip codes are there altogether in the Continental United States (excluding Hawaii, Alaska and Puerto Rico)?
db.dbw.aggregate(
  [
    { $match: { state: { $exists : true, $nin: ["HI", "AK"] } } },
    { $group : { "_id" : null, "count": { $sum: 1 } } }
  ]
)
# Query Result:
# { "_id" : null, "count" : 29078 }
# Answer: There are 29078 zipcodes in the Continental US.



##### Problem 5 #####
# How many zip codes are there altogether in New York, New Jersey, and Connecticut (NY, NJ, CT)?
db.dbw.aggregate(
  [
    { $match: { state: { $exists : true, $in: ["NY", "NJ", "CT"] } } },
    { $group : { "_id" : null, "count": { $sum: 1 } } }
  ]
)
# Query Result:
# { "_id" : null, "count" : 2398 }
# Answer: There are 2398 zipcodes in NY, NJ and CT.




##### Problem 6 
# Write two additional analytic queries of your choice for any state or group of states.
##### Problem 6-1
# According to Wikipedia(https://en.wikipedia.org/wiki/New_York_City), NYC ZIP codes include 100xx–104xx, 11004–05, 111xx–114xx, 116xx.
# How many zipcodes are in NYC?
db.dbw.find(
  { $or :
    [
      { _id : {$gte : "10000", $lte: "10499"} },
      { _id : {$gte : "11004", $lte: "11005"} },
      { _id : {$gte : "11100", $lte: "11499"} },
      { _id : {$gte : "11600", $lte: "11699"} }
    ]
  }
).count()
# Query Result: 178
# Answer: There are 178 zipcodes in NYC.

##### Problem 6-2
# How many people are in NYC's 178 zipcodes?
db.dbw.aggregate(
  [
    { $match: 
      { $or :
        [
          { _id : {$gte : "10000", $lte: "10499"} },
          { _id : {$gte : "11004", $lte: "11005"} },
          { _id : {$gte : "11100", $lte: "11499"} },
          { _id : {$gte : "11600", $lte: "11699"} }
        ]
      }
    },
    { $group : { "_id" : null, "count": { $sum: "$pop" } } }
  ]
)
# Query Result:
# { "_id" : null, "count" : 7324105 }
# Answer:
# According to this data, NYC's population was about 7.3 million in 2010. 
# This seems a bit less than numbers that US census Bureau provides (~8.3 million).
# I could not locate the source of the difference.

