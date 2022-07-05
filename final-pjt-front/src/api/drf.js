const HOST = 'https://mjyc-back.herokuapp.com/api/v1/'

const ACCOUNTS = 'accounts/'
const COMMUNITY = 'community/'
const COMMENTS = 'comments/'
const MOVIES = 'movies/'
const BASE_URL = 'https://api.themoviedb.org/3/'
const KEY = '?api_key=03f03c44041dd5b89d9605ef7395f631&language=ko-KR&page=1'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
    recommendUser: username => HOST + ACCOUNTS + 'profile/' + username + '/user_match/',
  },
  community: {
    likeReview: (reviewNum) => HOST + COMMUNITY + `reviews/${reviewNum}/like/`,
    reviews: () => HOST + COMMUNITY + 'reviews/',
    reviewDetail: (reviewNum) => HOST + COMMUNITY + `reviews/${reviewNum}`,
    comments: (reviewNum) => HOST + COMMUNITY + `reviews/${reviewNum}/comments/`,
    commentDetail: (reviewNum, commentNum) => HOST + COMMUNITY + `reviews/${reviewNum}/comments/${commentNum}`
  },
  movies: {
    movies: () => HOST + MOVIES,
    search: () => HOST + MOVIES + 'search/', 
  },
  nowplaying: {
    nowplaying: () => HOST + MOVIES + 'nowplaying/',
  },
  upcoming: {
    upcoming: () => BASE_URL + 'movie/upcoming' + KEY
  },
  popular: {
    popular: () => HOST + MOVIES + 'my_popular/'
  },
  tvshow: {
    tvshow: () => BASE_URL + 'tv/popular' + KEY
  },
  moviedetail: {
    moviedetail: (movieNum) => HOST + MOVIES + `${movieNum}/`,
    createmoviecomment: (movieNum) => HOST + MOVIES + `${movieNum}/` + COMMENTS,
    moviecommentdetail: (movieNum, commentPk) => HOST + MOVIES + `${movieNum}/` + COMMENTS + `${commentPk}/`,
  },
  likemovie: {
    likemovie: (movieNum) => HOST + MOVIES + `${movieNum}/` +'like/',
  },
}
