(() => {
    const httpRequest = new XMLHttpRequest();
  
    function handler() {
      if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 200) {
            treeConstructor()
        } else {
          alert('There was a problem with the request.');
        }
      }
    }

    httpRequest.onreadystatechange = handler;

    function treeConstructor(){
        var tree = d3.hierarchy(httpRequest.responseText)
        console.log(tree.data)
    }

    document
      .getElementById('ajaxButton')
      .addEventListener('click', () => {
        httpRequest.open('GET', '/test');
        httpRequest.send();
      });

  })();
