shakespeare.flatMap(
    lambda k: k.split()     # Split in words
).map(
    lambda k: k.lower()     # Remove case-sensitiveness issues
).filter(
    lambda k: k == 'murder' # Keep only this word
).count()


shakespeare.flatMap(
    lambda k: k.split() # Split in words
).filter(
    lambda k: len(k)>15 # Keep words longer than 15 characters
).take(10)





shakespeare.flatMap(
    lambda k: k.split()                 # Split in words
).filter(
    lambda k: not (set('.,-') & set(k)) # Drop words with special characters
).filter(
    lambda k: len(k)>15                 # Keep words longer than 15 characters
).collect()



shakespeare.flatMap(
    lambda k: k.split()                 # Split in words
).filter(
    lambda k: not (set('.,-') & set(k)) # Drop words with special characters
).reduce(
    keep_longest
)



words.map(
    lambda w: (w, 1)
).reduceByKey(
    lambda k1, k2: k1 + k2 
).sortBy(
    lambda t: t[1],
    ascending=False
).take(10)


# 1. Print then 10 most used words longer than 5 characters (case-insensitive)
words.filter(
    lambda w: len(w)>5
).map(
    lambda w: (w.lower(), 1)
).reduceByKey(
    lambda k1, k2: k1 + k2 
).sortBy(
    lambda t: t[1],
    ascending=False
).take(10)









# 2. How many words, longer than 5 characters, are used more than 100 times? (case-insensitive)
words.filter(
    lambda w: len(w)>5
).map(
    lambda w: (w.lower(), 1)
).reduceByKey(
    lambda k1, k2: k1 + k2 
).filter(
    lambda t: t[1]>200
).count()










ra_hist = gaia.groupBy(
    (
        func.floor(gaia.ra)
    ).alias('ra'),
).count().orderBy(
    'ra'
)

ra_hist.toPandas().set_index('ra').plot()

ra_hist = sqlc.sql("""
    SELECT FLOOR(ra) AS ra, COUNT(*) AS `count`
    FROM gaia
    GROUP BY 1
    ORDER BY 1
""")

ra_hist.toPandas().set_index('ra').plot()























