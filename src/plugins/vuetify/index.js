import 'vuetify/styles'

import { createVuetify } from 'vuetify'

export default createVuetify({
  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        dark: false,
        colors: {
          background: '#FAFAFA',
          surface: '#F5F5F5',    
          primary: '#139DF7',  
          secondary: '#D7FFB8',  
          error: '#B00020',
          info: '#2196F3',
          success: '#4CAF50',
          warning: '#FB8C00',
        },
        variables: {
          'font-family': 'Lato, sans-serif',
        }
      },
      dark: {
        dark: true,
        colors: {
          background: '#E9E9E9',
          surface: '#1E1E1E',
          primary: '#2b2b2b',
          secondary: '#03DAC6',
          error: '#CF6679',
          info: '#2196F3',
          success: '#4CAF50',
          warning: '#FB8C00',
        },
        variables: {
          'font-family': 'Lato, sans-serif',
        }
      }}
  },
})
