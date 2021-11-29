def get_scripts():
    return '''
        const run_btn = document.getElementById("run_btn");
        var alertPlaceholder = document.getElementById('liveAlertPlaceholder')
        run_btn.onclick = showAlert;

        function showAlert(event) {
            if (document.getElementById('data_file').files.length == 0){
                alertPlaceholder.innerHTML =  '<div class="alert alert-' + 'danger' + ' alert-dismissible" role="alert">' + 'Please select the dataset file' + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'
                return
            }

            if (document.getElementById("model_type").selectedIndex == 0){
                alertPlaceholder.innerHTML =  '<div class="alert alert-' + 'danger' + ' alert-dismissible" role="alert">' + 'Please select the Model' + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'
                return
            }
            document.getElementById("run_btn").innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>Running...'
            this.setAttribute("disabled","");
        }

    '''