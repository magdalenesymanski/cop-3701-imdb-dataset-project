# cop-3701-imdb-dataset-project

The database application being used during this project will be Oracle DB due to its intuitiveness and the fact that it is the recommended software for this project. Some of its benefits for this project are its lightweight use in any number of platforms and its vast library of resources to help in case the project becomes more complex. The IMDB dataset is a large dataset, and Oracle DB should be able to handle it with ease.

Course Project Part C (pre-de-normalization o_O):
<img width="951" height="730" alt="image" src="https://github.com/user-attachments/assets/2c870b0b-4907-4e7e-acb3-cdeb1b1347fb" />

Course Project Part D (de-normalized):
<img width="1078" height="845" alt="image" src="https://github.com/user-attachments/assets/27a44fe2-1b7e-464a-a1f8-50161d0e98a6" />
It was necessary to dissolve the associative relations for this part of the project. This unfortunately required me to dissolve the Country-Movie and Genre-Movie relations, and even more unfortunately to completely eliminate the user group, including user reviews. Movie Actor was left in, due to being necessary to the function of the schema, but will be left unpopulated. Being an associative relation, its coding process is beyond the scope of this class and definitely beyond the scope of my Python chops. However, it still leaves a solid portion of strong relations to populate and test the Oracle skills we've learned over the last few weeks.

Note from create_db.sql (Part D) explaining removal of foreign keys:

    /* 
        It is necessary that I remove all foreign key contraints from any relations following the prod_company relation,
        as the data limit that freesql imposes makes it impossoble to load all 80k+ records of my dataset, meanwhile
        many relations require all of the data to be loaded in order to reference foreign keys from another table.
        An impossible thing to remedy without starting over completely, I just made the decision to comment out the foreign 
        key references in order to prevent the error in the dataload.py file.
    */
