<div align="center">
    <a href="https://jeremyoo.github.io/free_to_play_games/">
        <h1>Spentrack_project</h1>
    </a>

Spentrack allows you to track your spending by classifying types of spendings!

[[ 🚧 Hosting under progress... 🚧 ]]


<img src = "./static/example_1.gif" width ="400" /> <img src = "./static/example_2.gif" width ="400" />

</div>


## Features
- View all the transactions
- View a transaction in detail
- Assign a trasaction to a merchant & a tag
- View spent amount by merchants & tags
- Add merchants & tags 
- Sort transactions by
    - date
    - amount
    - alphabetical
        
## Deployment

To deploy this project run

```bash
Your local machine terminal:
- git clone https://github.com/jeremyoo/spentrack_project.git
- createdb bucket_list (create db)
- psql -d spending_tracker -f db/spendings.sql (reset tables)
- python3 console.py (injecting sql data)
- flask run
```

## Technology
- python3
- Flask
- HTML5 / CSS3
- PostgreSQL & psycopg library

## Issue
Please submit any issue through following link [[Spentrack Issue]](https://github.com/jeremyoo/spentrack_project/issues).

## License
MIT
