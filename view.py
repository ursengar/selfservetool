from styles import get_style
from scripts import get_scripts
        # <!-- Compiled and minified CSS -->
        # <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

        # <!-- Compiled and minified JavaScript -->
        # <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

def get_header(style):
    return '''
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <style>
        ''' + style +'''
        </style>
        <title>Hello, world!</title>
    </head>
    '''

def get_body(footer_script):
     return '''
        <div class="container" id="main_con">
            <h1 class="display-3">Welcome to Self Serve Tool for ML Analytics</h1>
            <hr/>
            <div class="container">
                <p class="h3">How to use this tool:</p>
                <ul>
                    <li>Choose the your data file to upload.</li>
                    <li>Select the model.</li>
                    <li>Run the process to upload the file and run the model.</li>
                    <li>Download the result when it is available.</li>
                </ul>
                <hr/>
                <div class="container">
                    <div class="row">
                        <div class="col"></div>
                        <div class="col-6">
                            <div>
                                <label for="formFile" class="form-label">Upload dataset file:</label>
                                <input class="form-control" type="file" id="data_file">
                            </div>
                            <hr/>
                            <div>
                                <select class="form-select" aria-label="Default select example" id="model_type">
                                    <option selected>Select the model</option>
                                    <option value="1">Field Pulse</option>
                                    <option value="2">Sentiment Analysis</option>
                                    <option value="3">Model 3</option>
                                </select>
                            </div>
                            <div class="d-grid col-6 mx-auto" style="margin-top: 20px;">
                                <div id="liveAlertPlaceholder"></div>
                                <button class="btn btn-primary" type="button" id="run_btn">Run</button>
                            </div>

                        </div>
                        <div class="col"></div>
                    </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
        <script>
        ''' + footer_script + '''
        </script>
        '''

            # <h1>Upload File sto Blob</h1>
            # <!-- Large button groups (default and split) -->
            # <div class="btn-group">
            #     <button class="btn btn-secondary btn-lg dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            #         Large button
            #     </button>
            #     <ul class="dropdown-menu">
            #         ...
            #     </ul>
            # </div>
            # <form action="" method=post enctype=multipart/form-data>
            #     <p><input type=file name=file>
            #     <input type=submit value=Upload>
            # </form>



def get_page(header, body):
    return '''
        <!doctype html>
        <html>
        ''' + header + '''
        ''' + body +'''
        </html>
        '''

# def get_view():
#     return '''
#     <!doctype html>
#     <title>Upload new Filse</title>
#     <h1>Upload File sto Blob</h1>
#     <form action="" method=post enctype=multipart/form-data>
#       <p><input type=file name=file>
#          <input type=submit value=Upload>
#     </form>
    # '''
def get_view():
    return get_page(get_header(get_style()),get_body(get_scripts()))

def get_upload_file_view(ref):
    return '''
	    <!doctype html>
	    <title>File Link</title>
	    <h1>Uploaded File Link</h1>
	    <p>''' + ref + '''</p>
	    <img src="'''+ ref +'''">
	    '''