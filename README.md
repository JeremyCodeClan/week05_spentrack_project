<div align="center">
    <a href="https://jeremyoo.github.io/free_to_play_games/">
        <h1>Spentrack_project</h1>
    </a>

Spentrack allows you to track your spending by classifying types of spendings!

[[ 🚧 Hosting under progress... 🚧 ]]


<!-- <img src = "./src/static/example_1.gif" width ="450" /> <img src = "./src/static/example_2.gif" width ="450" /> -->

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
Please submit any issue through following link [[Free_To_Play Issue]](https://github.com/jeremyoo/free_to_play_games/issues).

## License
MIT
