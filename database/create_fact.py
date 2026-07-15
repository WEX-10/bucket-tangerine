# Tasks P1.1, P3.1, P4.3

from fact import Fact
from .provider import SQLiteConnectionProvider
from .helpers.database_helpers import fetch_fact_data

# TODO: (Task P4.3) Add category parameter
def create_fact(fact_text) -> Fact:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        # TODO: (Task P3.1) Add likes and dislikes counts to SQL query
        # TODO: (Task P4.3) Add category to SQL query
        cur.execute("INSERT INTO facts (fact) VALUES(?) RETURNING id, fact;",
                     (fact_text,)) # SQL query goes here
        fact_data = fetch_fact_data(cur)
        provider.commit()
        if not fact_data:
            return Fact(id=None, fact="", category=None, likes=0, dislikes=0) 
        
        return Fact(
            id=fact_data.id,
            fact= None,   
            likes=0,      # TODO: (Task P3.1) Add likes and dislikes counts to the Fact object
            dislikes=0,   
            category=None # TODO: (Task P4.3) Add category to returned fact
        )