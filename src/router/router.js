// router.js

import { createRouter, createWebHistory } from 'vue-router';
import Home from '../HomePage';
import HelloWorld from '../components/HTMLFundamentals/HelloWorld.vue';
import BlogPage from '../components/HTMLFundamentals/BlogPage.vue';
import Challenges from '../components/HTMLFundamentals/Challenges.vue';
import CSSGrid from '../components/HTMLFundamentals/CSSGrid';

import CSSLayout from '../components/CSSLayouts/CSSLayout';
import FlexBox from '../components/FlexBox/FlexBox';

import Natours from '../components/Natours/Natours';


const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/helloworld', name: 'HelloWorld', component: HelloWorld },
  { path: '/BlogPage', name: 'BlogPage', component: BlogPage },
  { path: '/Challenges', name: 'Challenges', component: Challenges },
  { path: '/CSSGrid', name: 'CSSGrid', component: CSSGrid },
  { path: '/CSSLayout', name: 'CSSLayout', component: CSSLayout },
  { path: '/FlexBox', name: 'FlexBox', component: FlexBox },
  { path: '/Natours', name: 'Natours', component: Natours }


];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
