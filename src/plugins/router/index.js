import { createRouter, createWebHistory } from 'vue-router'

import Error404 from '@/views/errors/Error404.vue'

import TestView from '@/views/TestView.vue'

import LessonView from '@/views/learn/LessonView.vue'

import MainView from '@/views/MainView.vue'
import CharactersView from '@/views/characters/CharactersView.vue'
import LeaderBoardView from '@/views/leaderboard/LeaderBoardView.vue'
import QuestView from '@/views/quests/QuestView.vue'
import ShopView from '@/views/shop/ShopView.vue'
import ProfileView from '@/views/profile/ProfileView.vue'

import LoginView from '@/views/auth/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: 'active',
  linkExactActiveClass: '',

  routes: [
    {
      path: '/lesson',
      name: 'lesson',
      component: LessonView
    },

    {
      path: '/',
      redirect: '/learn'
    },
    {
      path: '/learn',
      name: 'home',
      component: MainView
    },
    {
      path: '/characters',
      name: 'characters',
      component: CharactersView,
    },
    {
      path: '/leaderboard',
      name: 'leaderboard',
      component: LeaderBoardView,
    },
    {
      path: '/quests',
      name: 'quests',
      component: QuestView,
    },
    {
      path: '/shop',
      name: 'shop',
      component: ShopView,
    },
    {
      path: '/shop',
      name: 'shop',
      component: ShopView,
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
    },

    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/:catchAll(.*)',
      redirect: '/errors/404'
    },
    {
      path: '/errors/404',
      name: 'error404',
      component: Error404,
    },
    {
      path: '/test',
      name: 'test',
      component: TestView,
    },
  ],
})

export default router