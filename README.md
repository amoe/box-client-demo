# box-client-demo

Configure me with a JSON file, `credentials.json` in gitignore.

    {
        'client_id': 'zldx943gzs2wcymnqlawvstb2smrlx2z',
        'client_secret': 'zigkRwQKt8Z9MG7zkJXGD5VpfePF1vyz'
    }

These details are available in the box developer console.

This is to demonstrate use of the API.  See `requirements.txt` for the version
of the library being used.

This demo spins up a local HTTP server at port 49152 to answer the OAuth2
callback.  It will run a few calls on the folder defined at `TEST_FOLDER_ID` in
`run.py`.
