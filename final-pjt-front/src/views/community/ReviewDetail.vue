<template>
  <div class="review-detail-card w-75">
    <h3>Community</h3>
    <div class="container-fluid">
      <div class="d-flex justify-content-between">
        <div>
          <h1 class="text-left"> {{ review.title }}</h1>
          <p class="review_time">
            {{review.created_at|formatDate }} 작성됨 
            <br>
            {{review.updated_at|formatDate }} 최종 수정됨
          </p>
        </div>
        <div class="review_user">
          <router-link :to="{ name: 'profile', params: { username: review.user.username } }" class="text-decoration-none mx-4 text-center align-items-center" style="color: #fff;">
            <div>
              <img link :src="`https://mjyc-back.herokuapp.com${review.user.profile_image}`" alt="profile_image" class="profile_image mb-2 mx-auto" style="width: 100px;"><br>

            </div>
            <p >
              {{review.user.first_name}}
            </p>
          </router-link>
        </div>
      </div>
      <hr>

      <div class="content_box py-2 px-3">
        <p>
          {{ review.content }}
        </p>
      </div>
      <hr>
      <div v-if="isAuthor">
        <router-link :to="{ name: 'EditReview', params: { reviewNum } }">
          <button class="btn btn-sm btn-outline-success mx-1 my-2">수정</button>
        </router-link>
        <button class="btn btn-sm btn-outline-danger mx-1 my-2" @click="deleteReview(reviewNum)">삭제</button>
      </div>
      
      <div class="my-3">
        <button v-if="liked" class="btn btn-link" style="color: crimson;" @click="likeReview(reviewNum)" >
          <i class="fa-2x fa-solid fa-heart"></i>
        </button>
        <button v-else class="btn btn-link" style="color: crimson;" @click="likeReview(reviewNum)">
          <i class="fa-2x fa-regular fa-heart"></i>
        </button>
        {{ likeCount }} 명이 이 글을 좋아합니다.
      </div>
    

    </div>
    
    <CommentList :comments="review.comment_set"/>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/community/CommentList.vue'
  import moment from 'moment'


  export default {
    name: 'ReviewDetail',
    components: { CommentList },
    data() {
      return {
        reviewNum: this.$route.params.reviewNum,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'review', 'currentUser']),
      likeCount() {
        return this.review.like_users?.length
      },
      liked() {
        const array = [];
        for(var i in this.review.like_users) {
          array.push(Object.values(this.review.like_users)[i].username);
        }
        return array.includes(this.currentUser.username)
      }
    },
    filters: {
      formatDate (value) {
        console.log(value)
        if (value) {
          return moment(String(value)).format('MM/DD/YYYY hh:mm')
        }
      },
    },
    methods: {
      ...mapActions([
        'fetchReviewDetail',
        'likeReview',
        'deleteReview',
      ])
    },
    created() {
      this.fetchReviewDetail(this.reviewNum)
    },
  }
</script>

<style>
.review-detail-card {
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  padding: 2rem;
  width: 80%;
  max-width: 1000px;
  min-height: 100%;
  margin: auto;
  height: auto;
}

.review_time {
  text-align: left; 
  font-size: 0.8rem; 
  line-height: 1.8;
  padding: 0.3rem;
}

.content_box {
  text-align: left; 
  min-height: 15rem;
}
</style>
