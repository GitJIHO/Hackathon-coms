package com.study.board.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Data;

@Entity //table의미
@Data
public class Board {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) //identity라고 하면 jpa가 읽어들임
    private Integer id;

    private String title;

    private String content;
}

