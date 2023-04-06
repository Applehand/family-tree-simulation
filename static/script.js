(() => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = handler;

    function handler() {
      if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 200) {
            treeConstructor()
        } else {
          alert('There was a problem with the request.');
        }
      }
    }

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
