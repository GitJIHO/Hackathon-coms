package com.cums;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MainController {
    private final String FIVE_URL = "https://0a94-2001-e60-cb11-f4d6-8f1-98c4-eb3a-ec6.ngrok-free.app";
    private final String EIGHT_URL = "https://01c9-2001-e60-cb11-f4d6-8f1-98c4-eb3a-ec6.ngrok-free.app";

//    private final String FIVE_URL = "http://localhost:5000";
//    private final String EIGHT_URL = " http://localhost:8080";
    @GetMapping("/")
    public String index() {
        return "index";
    }
    @GetMapping("/redirectToText")
    public String redirectToText(){
        // 리디렉션
        return "redirect:" + FIVE_URL +"/text";
    }

    @GetMapping("/redirectToDiary")
    public String redirectToDiary() {
        return "redirect:/diary";
    }

    @GetMapping("/redirectToDiaryAnalysis")
    public String redirectToDiaryAnalysis() {
        return "redirect:" + FIVE_URL +"/file";
    }

    @GetMapping("/redirectToHobbyBoard")
    public String redirectToHobbyBoard() {
        return "redirect:question/list";
    }

    @GetMapping("/redirectToMain")
    public String redirectToMain(){
        return "redirect:" + EIGHT_URL;
    }
    @GetMapping("/redirectToAlbum")
    public String redirectToAlbum(){
        return "redirect:" + EIGHT_URL + "/album";
    }

    @GetMapping("/myInfo")
    public String myInfo() {
        return "myInfo";
    }

    @GetMapping("/redirectToQuestionForm")
    public String redirectToQuestionForm(){
        String filePath = EIGHT_URL;

        String url = readURLFromFile(filePath);
        return "redirect:" + url + "/question/create";
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