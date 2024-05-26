package com.cums.image;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AlbumController {

    // 앨범 페이지 요청을 처리하는 핸들러
    @GetMapping("/album")
    public String album(Model model) {
        // 이미지가 저장된 폴더 경로

        String folderPath = "src/main/resources/static/images";


        // 폴더 내의 이미지 파일 경로를 저장할 리스트
        List<String> imagePaths = new ArrayList<>();

        // 폴더 내의 파일 목록을 읽어와서 이미지 파일 경로 리스트에 추가
        File folder = new File(folderPath);
        File[] files = folder.listFiles();
        if (files != null) {
            Arrays.sort(files, (f1, f2) -> f2.getName().compareTo(f1.getName()));
            for (File file : files) {
                if (file.isFile()) {
                    // 파일의 상대 경로를 리스트에 추가
                    imagePaths.add("/images/" + file.getName());
                }
            }
        }

        // 이미지 파일 경로 리스트를 모델에 추가하여 Thymeleaf로 전달
        model.addAttribute("imagePaths", imagePaths);

        // 앨범 페이지로 이동
        return "album";
    }
}
