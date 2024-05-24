package com.cums.answer;


import com.cums.question.Question;
import com.cums.user.SiteUser;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;

@Getter
@Setter
@Entity
public class Answer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    @Column(columnDefinition = "TEXT")
    private String content;
    private LocalDateTime createDate;
    @ManyToOne //N:1의 관계를 나타냄 , 부모는 Question 자식은 Answer
    private Question question;
    @ManyToOne
    private SiteUser author;

    private LocalDateTime modifyDate;

}
