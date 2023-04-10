(() => {
    const httpRequest = new XMLHttpRequest();

    function handler() {
      if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 200) {
            treeConstructor(httpRequest.responseText)
        } else {
          alert('There was a problem with the request.');
        }
      }
    }

    httpRequest.onreadystatechange = handler;

    function treeConstructor(jsonData) {
      console.log(jsonData)
    }

    document
      .getElementById('ajaxButton')
      .addEventListener('click', () => {
        httpRequest.open('GET', '/test');
        httpRequest.send();
      });

  })();
