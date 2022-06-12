# Assignment 3

to run the Restful API

<p>clone this repository</p>
<pre><code>git clone https://github.com/Hruthvik/class15.git</code></pre>

<p>go to the repo</p>
<pre><code>cd class15</code></pre>

<p> build a docker image</p>
<pre><code>sudo docker build -t image1 .</code></pre>

<p> run the docker image</p>
<pre><code>sudo docker run -d -p 8080:80 image1:latest</code></pre>
<pre><code>sudo docker run  image1:latest</code></pre>

<p>To perform the GET and POST operations use these commands in a different terminal</p>

<pre><code>curl -X POST http://localhost:8080/numbers?new=123</code></pre>

<pre><code>curl -X GET http://localhost:8080/numbers/average”</code></pre>
<pre><code>curl -X GET http://localhost:8080/numbers/sum</code></pre>

