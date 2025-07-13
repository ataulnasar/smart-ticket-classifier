package com.you.ai.client;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.http.client.methods.*;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.*;
import org.apache.http.util.EntityUtils;

import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) throws Exception {
        String apiUrl = "http://localhost:5000/predict";
        String ticketText = "I need help with my invoice from last month.";

        // Prepare JSON body
        ObjectMapper mapper = new ObjectMapper();
        String json = mapper.writeValueAsString(new TicketRequest(ticketText));

        // Prepare HTTP request
        CloseableHttpClient client = HttpClients.createDefault();
        HttpPost request = new HttpPost(apiUrl);
        request.setHeader("Content-Type", "application/json");
        request.setEntity(new StringEntity(json, StandardCharsets.UTF_8));

        // Send and parse response
        CloseableHttpResponse response = client.execute(request);
        String responseBody = EntityUtils.toString(response.getEntity(), StandardCharsets.UTF_8);
        System.out.println("Predicted Category: " + responseBody);

        client.close();
    }

    static class TicketRequest {
        public String text;

        public TicketRequest(String text) {
            this.text = text;
        }
    }
}
