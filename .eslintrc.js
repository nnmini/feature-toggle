module.exports ={


    root: true,
    env:{
    node: true,
    jest:true,
    },

  parserOptions:{
    "parser": "@babel/eslint-parser",
    "ecmaVersion": 2021
  

  },
  extends:[
    'eslint:recommended',
    'plugin:vue/vue3-recommended'
  ],
  "rules": {
    // Add any custom ESLint rules or overrides here

  'vue/multi-word-component-names': 'off'
  
  }
}