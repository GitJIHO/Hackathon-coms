package com.cums;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

@Controller
public class MainController {
    private final String FIVE_URL = "C:\\hackerton\\Hackathon-cums\\5000.txt";
    private final String EIGHT_URL = "C:\\hackerton\\Hackathon-cums\\8080.txt";

    @GetMapping("/")
    public String index() {
        return "index";
    }
    @GetMapping("/redirectToText")
    public String redirectToText(){
        String filePath = FIVE_URL;

        String url = readURLFromFile(filePath);
        // 리디렉션
        return "redirect:" + url +"/text";
    }

    @GetMapping("/redirectToDiary")
    public String redirectToDiary() {

        String filePath = EIGHT_URL;

        String url = readURLFromFile(filePath);
        return "redirect:" + url +"/diary";
    }

    @GetMapping("/redirectToDiaryAnalysis")
    public String redirectToDiaryAnalysis() {
        String filePath = FIVE_URL;

        String url = readURLFromFile(filePath);
        return "redirect:" + url +"/file";
    }

    @GetMapping("/redirectToHobbyBoard")
    public String redirectToHobbyBoard() {
        return "redirect:question/list";
    }

    @GetMapping("/redirectToMain")
    public String redirectToMain(){
        String filePath = EIGHT_URL;

        String url = readURLFromFile(filePath);
        return "redirect:" + url;
    }
    @GetMapping("/redirectToAlbum")
    public String redirectToAlbum(){
        String filePath = EIGHT_URL;

        String url = readURLFromFile(filePath);
        return "redirect:" + url + "/album";
    }

    @GetMapping("/myInfo")
    public String myInfo() {
        return "myInfo";
    }

    // 파일에서 URL을 읽어오는 메서드
    private String readURLFromFile(String filePath) {
        StringBuilder content = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return content.toString();
    }


}