# foundCrop
A B2B Agricultural web Application. Find a crop everywhere you go !
# portfolio

## Architecture

### console

* Geston des Objets
    * Create
    * Update
    * destroy

```
$console.py
(crop)


* console command
    * quit
        permet de quitter la console s'emploie sans argument
        une fois quit atteint tout ce qui vient n'a plus d'importance

    * help
        ouvre la documentation:
        * quit                      : pour quitter
                                        *ex: quit*

        * help [command]            : afficher tout la documentation ou celle de la     
                                        commande *command* sauf help
                                        *ex: help*
                                        *ex: help create*

        * create <Model>              : creation de l'objet Model
                                        *ex: create User* 
                 [(key:val)]          : les parametres de l'objet separé par une virgule
                                        *ex: create User (name:John)*

        * show [Object]             : affiche tout les elements Objet de la base de     
                                        donnee et leurs tables ou l'objet *object* et tout ces tables
                                        *ex: show*
                                        *ex: show User*
               [id]                 : affiche l'objt *object* dont l'id est *id*
                                        *ex: show User 1457*
        
        * destroy <Model> <id>      : supprime l'objet *Model* d'identifiant *id*
        * update <Model> <(key:val)>: mis a jour de l'objet *Model*
        * count <Model>             : compte les tables du model
```
### file Storage
```
* directory: models
    * py file: __int__.py
        * attr: storage = FileLoding  ==> storage.loading()

* directory: models/engine
    * class: FileLoading
        * attr: __file_path (base.json)
        * attr: __database

        * show(self)
            * return ==> dictionary __database

        * new(self, obj)
            * add to __database (key:obj)
            * key = <obj.__class__.__name__>.<obj.id>

        * save(self)
            * json serialization

        * loading(self)
            * json deserialization
```

### web Static

* directory: templates
    * index.html
    * index.css
    * common.css

### Mysql storage

* sqlalchemy

```
* create foundCrop database
    * create
        * user: crop_dev
        * password: ***********
        * privilege: all for foundCrop

* directory: models/engine
    * Class: DBLoading
        * attr: __engine
        * attr: __session

        * __init__(self)

        * all(self, cls=None)
            * return dictionary
        
        * new(self, obj)
            * add new object obj
        
        * save(self)
            * commit
        
        * delete(self, obj=None)
            * remove object obj

        * loading(self)

        * get(self, cls, id)

        * count(self, cls=None)
```

### API

* path
    * /users
        * GET: all users
    * /users/<user.id>
        * (GET, DELETE, PUT, POST):user
    * /users/<user.id>/messages
        * (GET, DELETE, PUT, POST):all message for user
    * /users/<user.id>/messages/<message.id>
        * (GET, DELETE, PUT, POST):message for user
    * /users/<user.id>/messages/<destiny>
        * (GET, DELETE, PUT, POST):all message for user to destiny
    * /users/<user.id>/messages/<message.id>/<destiny>
        * (GET, DELETE, PUT, POST):message for user to destiny
    * /users/achats/<achat.id>
        * (GET, DELETE, PUT, POST):achat
    * /users/<user.id>/achats
        * (GET, DELETE, PUT, POST):all achats for user
    * /users/<user.id>/achats/<achat.id>
        * (GET, DELETE, PUT, POST):achat for user
    * /users/<user.id>/pictures
        * (GET, DELETE, PUT, POST):all pictures for user
    **********************************************
    * /promoters
        * GET: all promoter
    * /promoters/<promoter.id>
        * (GET, DELETE, PUT, POST): promoter
    * /promoters/<promoter.id>/messages
        * (GET, DELETE, PUT, POST): all message for promoter
    * /promoters/<promoter.id>/messages/<messsage.id>
        * (GET, DELETE, PUT, POST): message for promoter
    * /promoters/<promoter.id>/tradings
        * (GET, DELETE, PUT, POST): all trading for promoter
    * /promoters/<promoter.id>/tradings/<trader.id>
        * (GET, DELETE, PUT, POST): trading for promoter
    ***********************************************
    * /traders
        * GET: all trader
    * /traders/<trader.id>
        * (GET, DELETE, PUT, POST):trader
    * /traders/<trader.id>/messages
        * (GET, DELETE, PUT, POST):all message for trader
    * /traders/<trader.id>/messages/<message.id>
        * (GET, DELETE, PUT, POST): message for trader
    * /traders/<trader.id>/tradings
        * (GET, DELETE, PUT, POST):all trading for trader
    * /traders/<trader.id>/tradings/<promoter.id>
        * (GET, DELETE, PUT, POST): promoter to trader for trading
    * /traders/<trader.id>/produits
        * (GET, DELETE, PUT, POST): all produits for trader
    * /traders/<trader.id>/produits/<produit.id>
        * (GET, DELETE, PUT, POST): produits for trader
    ***********************************************
    * /produits
        * GET: all produit
    * /produits/<produit.id>
        * (GET, DELETE, PUT, POST):produit
    * /produits/<produit.id>/pictures
        * (GET, DELETE, PUT, POST):all pictures for produit
    * /produits/<produit.id>/pictures/<picture.id>
        * (GET, DELETE, PUT, POST):picture for produit
    ************************************************
    * /achats
        * GET: all achats
    * /achats/<achat.id>
        * (GET, DELETE, PUT, POST):achat
    ************************************************
    * /messages/<message.id>
        * (GET, DELETE, PUT, POST):message

* Class and functions
```
* directory: models

    Cette class represente les utilisateurs de facon general
    ---------------------------------------------------------------

    * class: User
        * id                                : string ==> uuid.uuid4()
        * firstName                         : string(128)
        * lastName                          : string(128)
        * username                          : string(128)
        * sexe                              : string(1)
        * contact                           : string(60)
        * email                             : string(128)
        * country                           : string(30)
        * city                              : string(30)
        * status                            : string(15) ==> (promoter, client, Trader)
        * password                          : string(128)
        * created                           : datetime

        * __init__(self, *args, **kwargs)
            * if kwargs is empty use args

        * __str__(self)
            * return ==> [<class name>] (<self.id>) <self.__dict__>

        * save(self)
            * save in the json file

        * to_dict(self)
            * return dictionary
    

    le promoteur class fils de User
    ----------------------------------------------------------------
    
    * Class: Promoter
        * profession                        : string(30)
    

    le trafic entre le promoteur et le commercant
    ----------------------------------------------------------------

    * Class: Trading
        * promo                             : Promoter.id
        * trade                             : Trader.id

        * __init__(self, **kwargs)

        * save(self)

        * to_dict(self)
    

    le commercant class fils de User
    ----------------------------------------------------------------

    * Class: Trader
        * gps                               : string(128)


    le produit
    ----------------------------------------------------------------

    * Class: Produit
        * id                                : string ==> uuid.uuid4
        * author                            : string ==> Trader.id
        * prd_name                          : string(128)
        * prd_quantity                      : int
        * unity_price                       : float
        * stock                             : int
        * stock_price                       : float

        * __init__(self, **kwargs)
        
        * save(self)

        * to_dict(self)


    les photos de produit 3 maximum, format: .png, .jpg, .jpeg
    ----------------------------------------------------------------

    * Class: Picture
        * file_path                         : string (.png, .jpg, .jpeg)
        * prd_id                            : string ==> Produit.id
        * user_id                           : string ==> User.id
        * type                              : int (0 ==> prd_id = "" or 1 user_id = "")

        * __init__(self, filepath, prd_id)

        * save(self)

        * to_dict(self)


    les achats
    ----------------------------------------------------------------

    - Class: Achat
        * id                                : string(128)
        * user_id                           : string User.id
        * prd_id                            : string Produit.id
        * quantity                          : int
        * price                             : float
        * date                              : datetime


    les messages
    -----------------------------------------------------------------

    * Class: Message
        * id                                : string ==> uuid.uuid4
        * user_id                           : string ==> User.id
        * destiny                           : string ==> User.id
        * text                              : string(4096)
        * publish                           : datetime
```

* API tierces
    * gmail
    * gps

### DATA MODEL 
        voir portfolio.drawio
