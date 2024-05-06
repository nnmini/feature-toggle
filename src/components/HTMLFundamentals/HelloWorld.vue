<template>
  <div>
    <article>
      <header>
        <!-- <h1>The Basic Language of the Web: HTML</h1>
    <h2>The Basic Language of the Web: HTML</h2>
    <h3>The Basic Language of the Web: HTML</h3>
    <h4>The Basic Language of the Web: HTML</h4>
    <h5>The Basic Language of the Web: HTML</h5>
    <h6>The Basic Language of the Web: HTML</h6> -->

        <h1>📘 The Code Magazine</h1>
        <nav>
          <router-link to="/BlogPage" class="right-margin">Blog</router-link>
          <router-link to="/Challenges" class="right-margin"
            >Challenges</router-link
          >
          <router-link to="/Flexbox" class="right-margin">Flexbox</router-link>
          <router-link to="/CSSGrid" class="right-margin">CSS Grid</router-link>
        </nav>

        <h2>The Basic Language of the Web: HTML</h2>
        <img
          src="./img/laura-jones.jpg"
          alt="author image"
          height="50"
          width="50"
        />
      </header>

      <p>Posted by <strong>Laura Jones</strong> on Monday, June 21st 2027</p>

      <img
        src="./img/post-img.jpg"
        alt="HTML code on a screen"
        width="500"
        height="200"
      />
      <p>
        All modern websites and web applications are built using three
        <em>fundamental</em>
        technologies: HTML, CSS and JavaScript. These are the languages of the
        web.
      </p>
      <p>
        In this post, let's focus on HTML. We will learn what HTML is all about,
        and why you too should learn it.
      </p>
      <h3>What is HTML?</h3>
      <p>
        HTML stands for <strong>H</strong>yperText <strong>M</strong>arkup
        <strong>L</strong>anguage. It's a markup language that web developers
        use to structure and describe the content of a webpage (not a
        programming language).
      </p>
      <p>
        HTML consists of elements that describe different types of content:
        paragraphs, links, headings, images, video, etc. Web browsers understand
        HTML and render HTML code as websites.
      </p>
      <p>In HTML, each element is made up of 3 parts:</p>
      <ol>
        <li>opening tag</li>
        <li>The closing tag</li>
        <li>The actual element</li>
      </ol>
      <p>
        You can learn more at the
        <a href="https://developer.mozilla.org/en-US/" target="_blank"
          >MDN Web Docs.</a
        >
      </p>
      <h3>Why should you learn HTML?</h3>
      <p>
        There are countless reasons for learning the fundamental language of the
        web. Here are 5 of them:
      </p>
      <ul>
        <li>To be able to use the fundamental web dev language</li>
        <li>
          To hand-craft beautiful websites instead of relying on tools like
          Worpress or Wix
        </li>
        <li>To build web applications</li>
        <li>To impress friends</li>
        <li>To have fun 😃</li>
      </ul>
      Hopefully you learned something new here. See you next time!
    </article>

    <aside>
      <h4>Related posts</h4>

      <ul>
        <li>
          <img src="./img/related-1.jpg" alt="Person programming" width="75" />
          <a href="#">How to Learn Web Development</a>
          <p>By Jonas Schmedtmann</p>
        </li>
        <li>
          <img
            src="./img/related-2.jpg"
            alt="Lightning"
            width="75"
            heigth="75"
          />
          <a href="#">The Unknown Powers of CSS</a>
          <p>By Jim Dillon</p>
        </li>
        <li>
          <img
            src="./img/related-3.jpg"
            alt="JavaScript code on a screen"
            width="75"
            height="75"
          />
          <a href="#">Why JavaScript is Awesome</a>
          <p>By Matilda</p>
        </li>
      </ul>
    </aside>
    <footer>Copyright &copy; 2027 by The Code Magazine.</footer>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.right-margin {
  margin-right: 10px;
}
</style>
