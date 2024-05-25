package com.cums;

import com.cums.question.QuestionService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class BoardApplicationTest {
    @Autowired
    private QuestionService questionService;

    @Test
    void testJpa(){
        for(int i = 1; i<= 300 ;i++){
            String subject = String.format("테스트 데이터입니다:[%03d]",i);
            String content = "내용무";
            this.questionService.create(subject,content,null);
        }

    }

}