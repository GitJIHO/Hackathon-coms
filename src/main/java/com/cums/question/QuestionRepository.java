package com.cums.question;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface QuestionRepository extends JpaRepository<Question,Integer> {//Question 엔티티로 레포지토리를 생성, 기본키 Integer
    Question findBySubject(String subject);

    Question findBySubjectAndContent(String subject,String content);

    List<Question> findBySubjectLike(String subject);
    Page<Question> findAll(Pageable pageable);

}
