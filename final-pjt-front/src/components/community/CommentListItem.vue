<template>
  <div>
    <div class="container" style="padding: 0rem;">
    <div class="px-4 d-flex justify-content-between">
      <router-link :to="{ name: 'profile', params: { username: comment.user.username } }" class="text-decoration-none mx-4 w-25 d-flex" style="color: #fff;">
        <img :src="`http://localhost:8000${comment.user.profile_image}`" class="profile_image img-fluid " alt="profile_image" style="width: 3rem; height: 3rem; margin: 0.5rem; margin-left: 0.8rem;">
        <div class="align-self-center m-auto">
          {{comment.user.first_name}}
        </div>
      </router-link>

      <div class="container-fluid align-self-center px-3" style="text-align: left;">
        {{comment.content}}
      </div>
      <div class="mx-2 comment_time align-self-center" style="width: 6rem;">
        <span v-if="currentUser.username === comment.user.username && !isEditing">

          <a @click="deleteReviewComment(payload)" 
          class="btn btn-danger text_decoration-underline"
          style="font-size: 0.6rem;"
          >삭제</a>
        </span>
      </div>
      <div class="comment_time">
        {{comment.created_at|formatDate }}
      </div>
    </div>
    <hr>

  </div>
    
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import moment from 'moment'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.comment.review,
        commentPk: this.comment.id,
        content: this.comment.content
      },
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
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateReviewComment', 'deleteReviewComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReviewComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style scoped>
.comment_time {
  text-align: left; 
  font-size: 0.9rem; 
  line-height: 1.8;
}
</style>